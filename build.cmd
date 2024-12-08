@echo off

set home=%~dp0
cd %home%

set image_name=
set tag=gcr.io/%image_name%

gcloud builds submit -t %tag% > %~dp0build.log

pause