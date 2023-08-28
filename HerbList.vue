<template>
  <div>
    <div class="header">
      <img class="logo" src="@/assets/herblogo.png" alt="Herb Logo" />
      <h1>Herb Store</h1>
      <input
        v-model="searchTerm"
        @input="filterHerbs"
        class="search-bar"
        type="text"
        placeholder="Search herbs..."
      />
    </div>
    <ul class="herb-list">
      <router-link
        v-for="herb in filteredHerbs"
        :key="herb.id"
        :to="'/herbs/' + herb.id"
        class="herb-item"
      >
        {{ herb.name }}
      </router-link>
    </ul>
  </div>
  <div class="header-buttons">
    <router-link to="/login" class="login-button">Login</router-link>
    <router-link to="/cart" class="cart-button">Cart</router-link>
  </div>
  <router-view></router-view>
<footer class="footer">
      <div class="contact-info">
        <strong>Contact:</strong> 0314-9949840
        <br />
        <strong>Email:</strong> info@herbstore.com
      </div>
      <div class="address">
        <strong>Address:</strong> 123 Balra Street, Bahter
      </div>
    </footer>

</template>

<script>
import axios from 'axios';

axios.defaults.baseURL = 'http://127.0.0.1:8000'; // Update the FastAPI URL

export default {
  data() {
    return {
      herbs: [],
      searchTerm: ''
    };
  },
  computed: {
    filteredHerbs() {
      if (!this.searchTerm) {
        return this.herbs;
      } else {
        const lowerCaseSearchTerm = this.searchTerm.toLowerCase();
        return this.herbs.filter(herb =>
          herb.name.toLowerCase().includes(lowerCaseSearchTerm)
        );
      }
    }
  },
  mounted() {
    this.fetchHerbs();
  },
  methods: {
    async fetchHerbs() {
      try {
        const response = await axios.get("/api/herbs");
        this.herbs = response.data;
      } catch (error) {
        console.error("Error fetching herbs:", error);
        console.log("Error details:", error.response);
      }
    }
    // ... your existing methods ...
  }
};
</script>

<style scoped>
.header {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
}

.logo {
  width: 100px; /* Adjust the width as needed */
  height: auto;
  margin-right: 10px;
}

h1 {
  font-size: 28px;
}

.herb-list {
  list-style: none;
  padding: 0;
}

.herb-item {
  margin-bottom: 10px;
  padding: 5px;
  background-color: #f0f0f0;
  border-radius: 5px;
  transition: background-color 0.2s ease;
}

.herb-item:hover {
  background-color: #e0e0e0;
}

.header-buttons {
  position: absolute;
  top: 0;
  right: 0;
  margin: 20px;
}

.login-button,
.cart-button {
  padding: 10px 20px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.login-button:hover,
.cart-button:hover {
  background-color: #45a049;
}

.search-bar {
  padding: 5px;
  margin-top: 10px;
  width: 100%;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.footer {
  background-color: #333;
  color: white;
  padding: 20px;
  text-align: center;
}

.contact-info,
.address {
  margin-bottom: 10px;
}

@media (max-width: 768px) {
  .footer {
    padding: 20px 0;
  }
}
</style>
