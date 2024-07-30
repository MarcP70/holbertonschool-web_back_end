import kue from "kue";

// Configure Kue avec Redis
const queue = kue.createQueue();

// Créaction d'un objet contenant les données du job
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a test message'
};

// Création d'un job dans la queue 'push_notification_code'
const job = queue.create("push_notification_code", jobData);

// Enregistrement du job
job
  .save(function (err) {
    if (err) {
      console.error("Erreur lors de la création du job:", err);
    } else {
      console.log("Notification job created:", job.id);
    }
  });


// Attache les gestionnaires d'événements globaux
queue.on('job complete', (id) => {
  console.log(`Notification job ${id} completed`);
});

queue.on('job failed', (id, err) => {
  console.log(`Notification job ${id} failed: ${err.message}`);
});
