INSERT INTO [dbo].[TestingLabeledData]
  ([Id]
      ,[TranscriptId]
      ,[SceneId]
      ,[IntentId]
      ,[Content]
      ,[Pass]
      ,[CreatedAt])
  VALUES
    (newid(), 'E89C4C5B-412D-434C-A7B6-02E92CD8FEAA', 'D74B9A51-F7B1-4CA3-BCF5-C3B27C4ECB2E', 1, 'intent1', 0, CURRENT_TIMESTAMP),
    (newid(), 'E89C4C5B-412D-434C-A7B6-02E92CD8FEAA', 'D74B9A51-F7B1-4CA3-BCF5-C3B27C4ECB2E', 2, 'intent2', 0, CURRENT_TIMESTAMP),
    (newid(), 'E89C4C5B-412D-434C-A7B6-02E92CD8FEAA', 'D74B9A51-F7B1-4CA3-BCF5-C3B27C4ECB2E', 3, 'intent3', 1, CURRENT_TIMESTAMP),
    (newid(), 'E89C4C5B-412D-434C-A7B6-02E92CD8FEAA', 'D74B9A51-F7B1-4CA3-BCF5-C3B27C4ECB2E', 4, 'intent4', 0, CURRENT_TIMESTAMP)