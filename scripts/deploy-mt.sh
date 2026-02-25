#!/bin/bash
echo "Deploying Property Intelligence Platform - Malta"
REGION="eu-south-1"
echo "Deploying to $REGION..."
sam deploy --region $REGION --stack-name property-intel-mt
echo "Deployment complete!"
