DROP TABLE [dbo].[TestingLabeledData];

SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[TestingLabeledData](
	[Id] [uniqueidentifier] NOT NULL,
	[TranscriptId] [uniqueidentifier] NOT NULL,
	[SceneId] [uniqueidentifier] NOT NULL,
	[IntentId] [int] NULL,
	[Content] [nvarchar](max) NULL,
	[Pass] [bit] NULL,
	[CreatedAt] [datetime] NULL,
 CONSTRAINT [PK_TestingLabeledData] PRIMARY KEY CLUSTERED
(
	[Id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY];


ALTER TABLE [dbo].[TestingLabeledData]  WITH CHECK ADD  CONSTRAINT [FK_TestingLabeledData_LabeledData_TranscriptId] FOREIGN KEY([TranscriptId])
REFERENCES [dbo].[LabeledData] ([Id])
ON DELETE CASCADE;

ALTER TABLE [dbo].[TestingLabeledData] CHECK CONSTRAINT [FK_TestingLabeledData_LabeledData_TranscriptId];

ALTER TABLE [dbo].[TestingLabeledData]  WITH CHECK ADD  CONSTRAINT [FK_TestingLabeledData_Scenes_SceneId] FOREIGN KEY([SceneId])
REFERENCES [dbo].[Scenes] ([Id]);

