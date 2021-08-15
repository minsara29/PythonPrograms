DROP TABLE [dbo].[IntentsResult];

SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[IntentsResult](
	[Id] [uniqueidentifier] NOT NULL,
	[ResultId] [uniqueidentifier] NOT NULL,
	[IntentId] [int] NULL,
	[IntentName] [nvarchar](max) NULL,
	[Pass] [bit] NULL,
	[CreatedAt] [datetime] NULL,
 CONSTRAINT [PK_IntentsResult] PRIMARY KEY CLUSTERED
(
	[Id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY];


ALTER TABLE [dbo].[IntentsResult]  WITH CHECK ADD  CONSTRAINT [FK_IntentsResult_TestingResults_ResultId] FOREIGN KEY([ResultId])
REFERENCES [dbo].[TestingResults] ([Id])
ON DELETE CASCADE;

ALTER TABLE [dbo].[IntentsResult] CHECK CONSTRAINT [FK_IntentsResult_TestingResults_ResultId];

