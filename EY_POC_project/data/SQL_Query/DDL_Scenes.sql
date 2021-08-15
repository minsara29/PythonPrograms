DROP TABLE [dbo].[Scenes];

SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[Scenes](
	[Id] [uniqueidentifier] NOT NULL,
	[ConversationId] [uniqueidentifier] NOT NULL,
	[Name] [nvarchar](500) NULL,
	[EstimatedCompletionTime] [time](7) NOT NULL,
	[Order] [int] NOT NULL,
	[Overview] [nvarchar](max) NULL,
 CONSTRAINT [PK_Scenes] PRIMARY KEY CLUSTERED
(
	[Id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY] ;