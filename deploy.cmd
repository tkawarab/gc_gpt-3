@echo off

set image_name=
set img=gcr.io/%image_name%

gcloud run deploy --image %img% --memory=4G > %~dp0deploy.log
pause