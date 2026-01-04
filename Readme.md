# ☁️ Secure Cloud Notes (AWS Serverless)

Full-stack serverless application for secure note-taking.

## 🚀 Architecture
The project follows a modern cloud-native architecture:
- **Frontend**: Single Page Application (SPA) hosted on **Amazon S3** and distributed via **CloudFront**.
- **Auth**: Secure user authentication handled by **Amazon Cognito** (JWT tokens).
- **Backend**: REST API managed by **Amazon API Gateway**.
- **Logic**: Serverless compute with **AWS Lambda** (Python 3.x).
- **Database**: NoSQL storage with **Amazon DynamoDB**.
- **Monitoring**: Real-time logs and error alarms via **CloudWatch**.

## 🛠 Features
- **CRUD Operations**: Create, Read, and Delete notes.
- **Security**: All API calls require a valid Cognito ID Token.
- **CORS**: Configured for secure cross-origin requests.
- **DevOps**: Integrated monitoring with CloudWatch Alarms for error tracking.

## 📦 Deployment
1. Deploy DynamoDB table `NotesTable` with PK:`userId` and SK:`noteId`.
2. Deploy Lambda with `AmazonDynamoDBFullAccess` permissions.
3. Setup API Gateway with Cognito Authorizer.
4. Update `index.html` with your `API_URL` and `CLIENT_ID`.