function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error("Jobs is not an array");
  }

  for (const job of jobs) {
    const newJob = queue
      .create("push_notification_code_3", job)

      .on("complete", (result) => {
        console.log(`Notification job ${newJob.id} completed`);
      })
      .on("failed", (error) => {
        console.log(`Notification job ${newJob.id} failed: ${error}`);
      })
      .on("progress", (progress) => {
        console.log(`Notification job ${newJob.id} ${progress}% complete`);
      });
    newJob.save((error) => {
      if (!error) {
        console.log(`Notification job created: ${newJob.id}`);
      }
    });
  }
}

export default createPushNotificationsJobs;
