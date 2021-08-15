DROP TABLE [dbo].[LearnerResults];

SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON
CREATE TABLE [dbo].[LearnerResults](
    [Id] [uniqueidentifier] NOT NULL,
    [TranscriptId] [uniqueidentifier] NOT NULL,
	[ModelId] [uniqueidentifier] NOT NULL,
	[IntentTraverse] [int] NULL,
	[IntentName] [nvarchar](50) NULL,
	[Result] [nvarchar](50) NULL,
	[Score] [float] NULL,
	[ProcessingTime] [time](7) NULL,
	[Version] [int] NULL,
	[CreatedAt] [timestamp] NULL
CONSTRAINT [PK_LearnerResults] PRIMARY KEY CLUSTERED
(
	[Id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] ;


ALTER TABLE [dbo].[LearnerResults]  WITH CHECK ADD  CONSTRAINT [FK_LearnerResults_LearnerTranscripts_TranscriptId] FOREIGN KEY([TranscriptId])
REFERENCES [dbo].[LearnerTranscripts] ([Id])
ON DELETE CASCADE;

ALTER TABLE [dbo].[LearnerResults] CHECK CONSTRAINT [FK_LearnerResults_LearnerTranscripts_TranscriptId];



