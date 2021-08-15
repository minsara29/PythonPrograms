DROP TABLE [dbo].[LearnerTranscripts];

SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON
CREATE TABLE [dbo].[LearnerTranscripts](
	[Id] [uniqueidentifier] NOT NULL,
	[UserId] [uniqueidentifier] NULL,
	[SceneId] [uniqueidentifier] NULL,
	[AttemptNo] [int] NULL,
	[Transcript] [nvarchar](max) NULL,
	[CreatedAt] [datetime] NULL,
CONSTRAINT [PK_LearnerTranscripts] PRIMARY KEY CLUSTERED
(
	[Id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY];


ALTER TABLE [dbo].[LearnerTranscripts]  WITH CHECK ADD  CONSTRAINT [FK_LearnerTranscripts_Scenes_SceneId] FOREIGN KEY([SceneId])
REFERENCES [dbo].[Scenes] ([Id])
ON DELETE CASCADE;

ALTER TABLE [dbo].[LearnerTranscripts] CHECK CONSTRAINT [FK_LearnerTranscripts_Scenes_SceneId];



