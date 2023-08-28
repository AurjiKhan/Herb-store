<template>
  <div class="herb-details">
    <img :src="herbImage" :alt="herb.name" class="herb-image" />
    <h2>{{ herb.name }}</h2>
    <p class="description">{{ herb.description }}</p>
    <h3>Uses:</h3>
    <p class="uses">{{ herb.uses }}</p>
    <h3>Origin:</h3>
    <p class="origin">{{ herb.origin }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HerbComponent', // Change to appropriate component name
  data() {
    return {
      herb: {},
      herbImage:''
    };
  },
  created() {
    this.fetchHerbDetails();

    this.herbImage = require('@/assets/Mint.png');
  },
  methods: {
    async fetchHerbDetails() {
      const herbId = this.$route.params.id; // Get the herb ID from route parameter
      try {
        const response = await axios.get(`/api/herbs/${herbId}`);
        this.herb = response.data;
      } catch (error) {
        console.error("Error fetching herb details:", error);
        console.log("Error details:", error.response);
      }
    }
  }
};
</script>

<style scoped>
.herb-details {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f7f7f7;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.description {
  font-weight: bold;
  margin-bottom: 10px;
}

.uses,
.origin {
  margin-top: 5px;
}

.uses::before,
.origin::before {
  content: "• ";
}
</style>
