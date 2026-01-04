# AWS Infrastructure Monitoring Dashboard

A real-time monitoring system for AWS resources built with AWS Lambda, S3, CloudWatch, and Flask.

## 🚀 Features

- **Real-time Monitoring**: Tracks EC2 instances, S3 buckets, and billing
- **Automated Collection**: Lambda function runs every 15 minutes
- **Visual Dashboard**: Beautiful web interface with charts
- **Historical Trends**: View metrics over time
- **Cost Tracking**: Monitor estimated AWS charges

## 🛠️ Technologies

- **Backend**: Python, Flask
- **AWS Services**: Lambda, S3, CloudWatch, EventBridge
- **Infrastructure**: Terraform
- **Frontend**: HTML, CSS, JavaScript, Chart.js
- **Region**: ap-south-1 (Mumbai)

## 📋 Prerequisites

- AWS Account (Free Tier)
- AWS CLI configured
- Python 3.11+
- Terraform 1.0+

## 🚦 Setup Instructions

### 1. Clone and Setup
```bash
git clone https://github.com/arpanmahata-dev/aws-monitoring-dashboard.git
cd aws-monitoring-dashboard
```

### 2. Configure AWS
```bash
aws configure
# Enter your AWS credentials
# Region: ap-south-1
```

### 3. Deploy Infrastructure
```bash
cd terraform
terraform init
terraform apply
# Note the bucket name from output
```

### 4. Update Dashboard Config

Edit `dashboard/app.py` and update BUCKET_NAME with your bucket name.

### 5. Run Dashboard
```bash
cd dashboard
pip install -r requirements.txt
python app.py
```

### 6. Access Dashboard

Open browser: `http://localhost:5000`

## 📊 Project Structure
````
aws-monitoring-dashboard/
├── lambda/
│   ├── collector.py           # Lambda function for metrics collection
│   └── requirements.txt       # Lambda dependencies
├── dashboard/
│   ├── app.py                 # Flask application
│   ├── templates/
│   │   └── dashboard.html     # Dashboard UI
│   └── requirements.txt       # Dashboard dependencies
├── terraform/
│   └── main.tf                # Infrastructure as Code
└── README.md


---------------------------------------------------

🧹 Cleanup
To avoid charges, destroy resources when done:

cd terraform
terraform destroy
````

## 👨‍💻 Author

**Arpan Mahata**
- GitHub: [@arpanmahata-dev](https://github.com/arpanmahata-dev)
- LinkedIn: [arpanmahato](https://linkedin.com/in/arpanmahato)
- Email: arpanmahato2001@gmail.com

## 📝 License

This project is part of my DevOps portfolio and is free to use for learning purposes.

## 🙏 Acknowledgments

Built as part of DevOps learning journey to demonstrate:
- Cloud architecture design
- Infrastructure as Code
- Serverless computing
- Monitoring and observability
- Full-stack development

---

⭐ If you found this project helpful, please give it a star!
````

Push to GitHub (15 minutes)

Initialize Git Repository
````bash
# Navigate to project root
cd C:\Users\cptc0$MIC\Desktop\DevOps-Projects\aws-monitoring-dashboard

# Initialize git
git init

# Create .gitignore
````

**Create `.gitignore` file:**
````
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
*.egg-info/

# Terraform
.terraform/
*.tfstate
*.tfstate.backup
terraform.tfvars
*.zip

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# AWS
.aws/
response.json

# Environment
.env
````

### : Commit and Push
````bash
# Add all files
git add .

# Commit
git commit -m "Initial commit: AWS Monitoring Dashboard"

# Create repository on GitHub
# Go to github.com → New Repository → Name it "aws-monitoring-dashboard"

# Add remote
git remote add origin https://github.com/arpanmahata-dev/aws-monitoring-dashboard.git

# Push
git branch -M main
git push -u origin main
````

---

## 🎉 SUCCESS CHECKLIST

Mark these as you complete them:

- [ ] ✅ All project files created
- [ ] ✅ AWS credentials configured
- [ ] ✅ Lambda function deployed
- [ ] ✅ S3 bucket created and populated
- [ ] ✅ EventBridge rule running every 15 minutes
- [ ] ✅ Dashboard running locally
- [ ] ✅ Can see metrics in dashboard
- [ ] ✅ Charts displaying data
- [ ] ✅ Test EC2 instance created (optional)
- [ ] ✅ README documentation complete
- [ ] ✅ Code pushed to GitHub

---

## 📸 Screenshots to Take for Resume/Portfolio

Take these screenshots:

1. **Dashboard homepage**
   <img width="1893" height="648" alt="image" src="https://github.com/user-attachments/assets/f1d5f23c-e103-432d-8e9e-1e25acdfa56d" />
   
2. **Chart with data**
   <img width="1841" height="845" alt="image" src="https://github.com/user-attachments/assets/d77af067-b0c8-4a99-94c4-02f4807f7051" />
   
3. **AWS Lambda console**
<img width="1884" height="611" alt="image" src="https://github.com/user-attachments/assets/560b7147-6ae4-4719-8c39-fd5c883fe83c" />

   
4. **S3 bucket** 
<img width="1885" height="724" alt="image" src="https://github.com/user-attachments/assets/0d2d0e1d-3a87-4af8-afe7-9bffa5056200" />

5. **EventBridge rule** 
<img width="1449" height="674" alt="image" src="https://github.com/user-attachments/assets/89674f39-7c19-48b8-b157-7d722bc10b99" />
<img width="993" height="685" alt="image" src="https://github.com/user-attachments/assets/7649ad5b-dec4-4532-8d65-5db14f553342" />
<img width="913" height="620" alt="image" src="https://github.com/user-attachments/assets/a6efd216-e0b4-4fac-9784-9bb739c4f160" />
<img width="901" height="895" alt="image" src="https://github.com/user-attachments/assets/52acac92-03b2-4a60-93e1-e1ab88e85b25" />
<img width="859" height="788" alt="image" src="https://github.com/user-attachments/assets/cd0ce42a-169b-4ddb-89cf-cb28251b0fec" />

6. **Terraform apply output**
  <img width="1235" height="468" alt="image" src="https://github.com/user-attachments/assets/dc22c24e-3317-453f-b306-bc83e3e81cc1" />


---
AWS Infrastructure Monitoring Dashboard
- Developed automated monitoring system using AWS Lambda, S3, and CloudWatch
- Implemented serverless architecture collecting metrics every 15 minutes
- Built real-time dashboard with Flask displaying EC2, S3, and billing metrics
- Deployed infrastructure using Terraform (IaC) in ap-south-1 region
- Achieved 100% Free Tier usage with automated data lifecycle management
````

---

## 🆘 Common Issues and Solutions

### Issue 1: "boto3 module not found"
````bash
pip install boto3
````

### Issue 2: Lambda can't write to S3
- Check IAM permissions in Terraform
- Verify bucket name in Lambda environment variables

### Issue 3: Dashboard shows no data
- Wait 15 minutes for first Lambda execution
- Or manually test Lambda in AWS Console
- Check S3 for metrics/ folder

### Issue 4: Terraform apply fails
````bash
terraform destroy
terraform init
terraform apply
````

### Issue 5: Can't access dashboard
- Check if Flask is running: `python app.py`
- Try `http://127.0.0.1:5000` instead of localhost
- Check firewall settings

---

## 📞 Need Help?

If you're stuck at any step:

1. **Check CloudWatch Logs** - Most errors are logged there
2. **Verify AWS Credentials** - Run `aws sts get-caller-identity`
3. **Check Terraform State** - Run `terraform state list`
4. **Test Components Individually** - Lambda → S3 → Dashboard

---

🎊 **CONGRATULATIONS!** 

This project demonstrates:

- ✅ AWS Lambda (Serverless)
- ✅ Infrastructure as Code (Terraform)
- ✅ Full-stack Development (Flask + HTML/JS)
- ✅ Cloud Architecture Design
- ✅ Automation & Scheduling

---


