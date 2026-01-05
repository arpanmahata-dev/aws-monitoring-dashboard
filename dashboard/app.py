from flask import Flask, render_template, jsonify
import boto3
import json
from datetime import datetime
import os

app = Flask(__name__)

# AWS Configuration
AWS_REGION = 'ap-south-1'
BUCKET_NAME = os.environ.get('BUCKET_NAME', 'aws-monitoring-metrics-82e9d6ef')  # Use your bucket name from Terraform output

# Initialize AWS clients
s3 = boto3.client('s3', region_name=AWS_REGION)

@app.route('/')
def dashboard():
    """Main dashboard page"""
    try:
        metrics = get_latest_metrics()
        return render_template('dashboard.html', metrics=metrics)
    except Exception as e:
        print(f"Error loading dashboard: {str(e)}")
        return render_template('dashboard.html', metrics={}, error=str(e))

@app.route('/api/metrics')
def api_metrics():
    """API endpoint for metrics data"""
    try:
     # Get all metrics files (last 24 hours)
        response = s3.list_objects_v2(
            Bucket=BUCKET_NAME,
            Prefix='metrics/',
            MaxKeys=100
        )
        

        metrics_list = []
        
        if 'Contents' in response:
            # Sort by last modified (newest first)
            objects = sorted(response['Contents'], key=lambda x: x['LastModified'], reverse=True)
            # Get up to 24 most recent files (one per hour)
            for obj in objects[:24]:
                try:
                    data = s3.get_object(Bucket=BUCKET_NAME, Key=obj['Key'])
                    metrics = json.loads(data['Body'].read())
                    metrics_list.append(metrics)
                except Exception as e:
                    print(f"Error reading {obj['Key']}: {str(e)}")
                    continue
        
        return jsonify({
            'success': True,
            'count': len(metrics_list),
            'metrics': metrics_list
        })
        

    except Exception as e:
        print(f"Error in API: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/latest')
def api_latest():
    """Get only the latest metrics"""
    try:
        metrics = get_latest_metrics()
        return jsonify({
            'success': True,
            'metrics': metrics
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


        
        # Get the most recent file
        latest_obj = max(response['Contents'], key=lambda x: x['LastModified'])
        
        # Read the file content
        obj_data = s3.get_object(Bucket=BUCKET_NAME, Key=latest_obj['Key'])
        metrics = json.loads(obj_data['Body'].read())
        
        return metrics
        
    except Exception as e:
        print(f"Error getting latest metrics: {str(e)}")
        return {
            'timestamp': datetime.now().isoformat(),
            'ec2_instances': {'total': 0, 'running': 0, 'stopped': 0},
            's3_buckets': {'total': 0},
            'billing': {'estimated_charges': 0.0}
        }

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    print(f"Starting dashboard for bucket: {BUCKET_NAME}")
    app.run(host='0.0.0.0', port=5000, debug=True)