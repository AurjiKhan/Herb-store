<template>
  <div class="cart-page">
    <h2>Your Cart</h2>
    <div v-if="cartItems.length > 0">
      <div v-for="(item, index) in cartItems" :key="index" class="cart-item">
        <img :src="item.image" alt="Product" class="cart-item-image" />
        <div class="cart-item-details">
          <h3>{{ item.name }}</h3>
          <p>Price: ${{ item.price }}</p>
        </div>
        <button class="remove-button" @click="removeItem(index)">Remove</button>
      </div>
      <div class="cart-total">
        <p>Total: ${{ calculateTotal() }}</p>
        <button class="checkout-button" @click="navigateToLogin">Checkout</button>
      </div>
    </div>
    <div v-else>
      <p>Your cart is empty.</p>
    </div>
    <div class="herb-list">
      <h2>Herbs</h2>
      <div v-for="(herb, index) in herbs" :key="index" class="herb-item">
        <img :src="herb.image" alt="Herb" class="herb-image" />
        <div class="herb-details">
          <h3>{{ herb.name }}</h3>
          <p>Price: ${{ herb.price }}</p>
        </div>
        <button class="add-button" @click="addItemToCart(herb)">Add to Cart</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter();

const cartItems = ref([

]);

const herbs = [
  { name: 'Lavender', price: 4, image: '/assets/Lavender.png' },
  { name: 'Rosemary', price: 3, image: '/assets/Rosemary.png' },
  { name: 'Mint', price: 1, image: '@/assets/Mint.png' },
  { name: 'Chamomile', price: 2, image: '/assets/Chamomile.png' },
  { name: 'Thyme', price: 2, image: '/assets/Thyme.png' },
];

function calculateTotal() {
  return cartItems.value.reduce((total, item) => total + item.price, 0);
}

function removeItem(index) {
  cartItems.value.splice(index, 1);
}

function addItemToCart(herb) {
  cartItems.value.push({ name: herb.name, price: herb.price, image: herb.image });
}
function navigateToLogin() {
  // Use the router to navigate to the login page
  router.push('/login'); // Replace '/login' with your actual login page route
}
</script>

<style scoped>
.cart-page {
  padding: 20px;
}

.cart-item {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.cart-item-image {
  width: 80px;
  height: 80px;
  object-fit: cover;
  border-radius: 8px;
  margin-right: 10px;
}

.cart-item-details {
  flex: 1;
}

.remove-button {
  background-color: #f44336;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 5px 10px;
  cursor: pointer;
}

.remove-button:hover {
  background-color: #d32f2f;
}

.cart-total {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
}

.checkout-button {
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  cursor: pointer;
}

.checkout-button:hover {
  background-color: #45a049;
}
.herb-list {
  margin-top: 40px;
}

.herb-item {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.herb-image {
  width: 80px;
  height: 80px;
  object-fit: cover;
  border-radius: 8px;
  margin-right: 10px;
}

.herb-details {
  flex: 1;
}

.add-button {
  background-color: #1976d2;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 5px 10px;
  cursor: pointer;
}

.add-button:hover {
  background-color: #1565c0;
}
</style>
