DROP TABLE [dbo].[LabeledData];

SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[LabeledData](
	[Id] [uniqueidentifier] NOT NULL,
	[SceneID] [uniqueidentifier] NOT NULL,
	[Transcript] [nvarchar](max) NOT NULL,
 CONSTRAINT [PK_LabeledData] PRIMARY KEY CLUSTERED
(
	[Id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY];


ALTER TABLE [dbo].[LabeledData]  WITH CHECK ADD  CONSTRAINT [FK_LabeledData_Scenes_SceneId] FOREIGN KEY([SceneId])
REFERENCES [dbo].[Scenes] ([Id])
ON DELETE CASCADE;

ALTER TABLE [dbo].[LabeledData] CHECK CONSTRAINT [FK_LabeledData_Scenes_SceneId];


