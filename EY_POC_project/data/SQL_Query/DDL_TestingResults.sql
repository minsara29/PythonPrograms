DROP TABLE [dbo].[TestingResults];

SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[TestingResults](
	[Id] [uniqueidentifier] NOT NULL,
	[TranscriptId] [uniqueidentifier] NOT NULL,
	[ModelId] [int] NOT NULL,
	[IntentTraverse] [int] NULL,
	[Score] [float] NULL,
	[ProcessingTime] [time](7) NULL,
	[Version] [int] NULL,
	[CreatedAt] [datetime] NULL,
CONSTRAINT [PK_TestingResults] PRIMARY KEY CLUSTERED
(
	[Id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY];


ALTER TABLE [dbo].[TestingResults]  WITH CHECK ADD  CONSTRAINT [FK_TestingResults_LabeledData_TranscriptId] FOREIGN KEY([TranscriptId])
REFERENCES [dbo].[LabeledData] ([Id])
ON DELETE CASCADE;

ALTER TABLE [dbo].[TestingResults] CHECK CONSTRAINT [FK_TestingResults_LabeledData_TranscriptId];

ALTER TABLE [dbo].[TestingResults]  WITH CHECK ADD  CONSTRAINT [FK_TestingResults_MLModelsName_ModelId] FOREIGN KEY([ModelId])
REFERENCES [dbo].[MLModelsName] ([Id]);

