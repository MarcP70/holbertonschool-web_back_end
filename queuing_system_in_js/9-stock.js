import express from "express"; // Importation du framework Express pour créer le serveur HTTP
import { createClient } from "redis"; // Importation de la bibliothèque Redis pour gérer la connexion à Redis
import { promisify } from "util"; // Importation de la bibliothèque util pour utiliser promisify

// Définition d'une liste de produits disponibles
const listProducts = [
  { id: 1, name: "Suitcase 250", price: 50, stock: 4 },
  { id: 2, name: "Suitcase 450", price: 100, stock: 10 },
  { id: 3, name: "Suitcase 650", price: 350, stock: 2 },
  { id: 4, name: "Suitcase 1050", price: 550, stock: 5 },
];

// Fonction pour récupérer un produit par son ID
function getItemById(id) {
  return listProducts.find((obj) => obj.id === id);
}

const app = express(); // Création de l'application Express
const client = createClient(); // Création du client Redis

// Fonction pour réserver le stock d'un produit par son ID
function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock); // Enregistrement du stock réservé dans Redis
}

// Promisification de la fonction client.get pour utiliser async/await
const clientGet = promisify(client.get).bind(client);

// Fonction asynchrone pour obtenir le stock réservé actuel d'un produit par son ID
async function getCurrentReservedStockById(itemId) {
  const stock = await clientGet(`item.${itemId}`);
  return stock;
}

// Route pour lister tous les produits disponibles
app.get("/list_products", (req, res) => {
  const response = listProducts.map((obj) => ({
    itemId: obj.id,
    itemName: obj.name,
    price: obj.price,
    initialAvailableQuantity: obj.stock,
  }));
  res.json(response); // Retourne la liste des produits en format JSON
});

// Route pour obtenir les détails d'un produit par son ID
app.get("/list_products/:itemId", async (req, res) => {
  const item = getItemById(Number(req.params.itemId)); // Récupération du produit par ID
  if (!item) {
    return res.json({ status: "Product not found" }); // Si le produit n'existe pas, retourne un message d'erreur
  }

  const currentReservedStock = await getCurrentReservedStockById(req.params.itemId); // Récupération du stock réservé actuel
  const response = {
    itemID: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity: item.stock - Number(currentReservedStock || 0), // Calcul du stock disponible actuel
  };

  res.json(response); // Retourne les détails du produit en format JSON
});

// Route pour réserver un produit par son ID
app.get("/reserve_product/:itemId", async (req, res) => {
  const item = getItemById(Number(req.params.itemId)); // Récupération du produit par ID
  if (!item) {
    return res.json({ status: "Product not found" }); // Si le produit n'existe pas, retourne un message d'erreur
  }

  const currentReservedStock = await getCurrentReservedStockById(req.params.itemId); // Récupération du stock réservé actuel
  const itemInStock = item.stock - Number(currentReservedStock || 0); // Calcul du stock disponible actuel

  if (itemInStock <= 0) {
    return res.json({ status: "Not enough stock available", itemId: req.params.itemId }); // Si le stock est insuffisant, retourne un message d'erreur
  } else {
    reserveStockById(req.params.itemId, Number(currentReservedStock || 0) + 1); // Réserve le stock en ajoutant 1
    res.json({ status: "Reservation confirmed", itemId: req.params.itemId }); // Retourne un message de confirmation de réservation
  }
});

// Lancement du serveur sur le port 1245
app.listen(1245, () => {
  console.log('Server is running on port 1245');
});
