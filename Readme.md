## 概要
openaiのgpt-3を使用したチャット画面
質問の入力を日本語で受付け、gpt-3のAPIへ連携し、AIの回答を得ます。

## 目的
gpt-3の検証
※ChatGPTがリリースされる前に行った検証

## アーキテクチャ
### 言語
- front (python flask)
- backend-api (python flask)

### 外部API連携
- OpenAI gpt-3 api
- Deepl translate api

### CICD
-  Build
    - Docker Image Build
    - GCP Build　⇒　Artifact Registry
-  Deploy
    - GCP Deoploy　⇒　CloudRun

### 環境変数
- OPENAI_API_KEY
    - openaiのAPIキーを設定する
- DEEPL_API_AUTH_KEY
    - deeplのAPIキーを設定する