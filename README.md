# Deploy your PyWebIO app to cloud platform

## GAE

### Create project
Go [Google Cloud App Engine](https://console.cloud.google.com/appengine), and create a new project.

### Open Cloud Shell
Open Cloud Shell by clicking the Activate Cloud Shell button in the navigation bar in the upper-right corner of the console.

### Get app code

In Cloud Shell, enter the following:

```bash
git clone https://github.com/wang0618/pywebio-in-cloud.git
```

### Deploying with Cloud Shell
To deploy your app enter the following:

```bash
cd pywebio-in-cloud
gcloud app deploy app.yaml --project pywebio-demo
```

### Visit your app

To view your application in the web browser run:
```bash
gcloud app browse
```

Then you will get a link to your app.

NOTE:
 - The standard environment of GAE doesn't support websocket, so you need to use `pywebio.platform.tornado_http.start_server()` or `pywebio.platform.flask.start_server()` or `pywebio.platform.django.start_server()` to start server which communicates with the browser using HTTP protocol. The flexible environment does support websocket, but it has no free quota. For more info, see https://cloud.google.com/appengine/docs/the-appengine-environments
 - If you just want to use the free quota of GAE and don't want to be charged, go to the [Billing page](https://console.cloud.google.com/billing/projects) to disable billing
 - To delete the project, see https://cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects
