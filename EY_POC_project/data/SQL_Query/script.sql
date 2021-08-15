/****** Object:  Table [dbo].[LabeledData]    Script Date: 8/13/2021 8:22:24 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[LabeledData](
	[id] [uniqueidentifier] NOT NULL,
	[scene_id] [uniqueidentifier] NOT NULL,
	[transcript] [nvarchar](max) NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[LearnerResults]    Script Date: 8/13/2021 8:22:24 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[LearnerResults](
	[id] [uniqueidentifier] NOT NULL,
	[scene_id] [uniqueidentifier] NOT NULL,
	[model_id] [uniqueidentifier] NOT NULL,
	[transcript_id] [uniqueidentifier] NOT NULL,
	[intent_traverse] [int] NULL,
	[intent_name] [nvarchar](50) NULL,
	[result] [nvarchar](50) NULL,
	[score] [float] NULL,
	[processing_time] [time](7) NULL,
	[version] [int] NULL,
	[created_at] [timestamp] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[LearnerTranscripts]    Script Date: 8/13/2021 8:22:24 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[LearnerTranscripts](
	[id] [uniqueidentifier] NOT NULL,
	[user_id] [uniqueidentifier] NULL,
	[scene_id] [uniqueidentifier] NULL,
	[attempt_no] [int] NULL,
	[transcripts] [nvarchar](max) NULL,
	[created_at] [datetime] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[MLModelsName]    Script Date: 8/13/2021 8:22:24 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[MLModelsName](
	[id] [uniqueidentifier] NOT NULL,
	[name] [nvarchar](50) NOT NULL,
	[description] [nvarchar](50) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Scenes]    Script Date: 8/13/2021 8:22:24 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Scenes](
	[id] [uniqueidentifier] NOT NULL,
	[conversation_id] [uniqueidentifier] NOT NULL,
	[sequence_number] [int] NULL,
	[expert_answer] [nvarchar](max) NOT NULL,
	[pass_threshold] [float] NOT NULL,
	[key_part1] [nvarchar](50) NULL,
	[key_part2] [nvarchar](50) NULL,
	[estimated_time] [time](7) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TestingLabeledData]    Script Date: 8/13/2021 8:22:24 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TestingLabeledData](
	[id] [uniqueidentifier] NOT NULL,
	[scene_id] [uniqueidentifier] NOT NULL,
	[transcript_id] [uniqueidentifier] NOT NULL,
	[intent_id] [int] NULL,
	[content] [nvarchar](max) NULL,
	[pass] [nvarchar](max) NULL,
	[created_at] [datetime] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TestingResults]    Script Date: 8/13/2021 8:22:24 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TestingResults](
	[id] [uniqueidentifier] NOT NULL,
	[scene_id] [uniqueidentifier] NOT NULL,
	[model_id] [uniqueidentifier] NOT NULL,
	[transcript_id] [uniqueidentifier] NOT NULL,
	[intent_traverse] [int] NULL,
	[intent_name] [nvarchar](max) NULL,
	[result] [nvarchar](50) NULL,
	[score] [float] NULL,
	[processing_time] [time](7) NULL,
	[version] [int] NULL,
	[accuracy] [float] NULL,
	[pricision] [float] NULL,
	[f_score] [float] NULL,
	[specificity] [float] NULL,
	[created_at] [datetime] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TrainingLabeledData]    Script Date: 8/13/2021 8:22:24 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TrainingLabeledData](
	[id] [uniqueidentifier] NOT NULL,
	[scene_id] [uniqueidentifier] NOT NULL,
	[transcript_id] [uniqueidentifier] NOT NULL,
	[intent_id] [int] NULL,
	[content] [nvarchar](max) NULL,
	[pass] [tinyint] NULL,
	[created_at] [datetime] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
