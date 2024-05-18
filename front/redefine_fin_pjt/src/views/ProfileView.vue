<template>
    <div>
        <h1>Profile Page</h1>
        <p>username: {{ userProfile.value }}</p>
    </div>
</template>

<script setup>

import { ref, onMounted } from 'vue'
import { useProfileStore } from '@/stores/profile';

const profilestore = useProfileStore()
const userProfile = ref(null)

onMounted(() => {

    axios({
      method: 'get',
      url: `${profilestore.API_URL}/accounts/profile/`,
      headers: {
        Authorization: `Token ${profilestore.token}`,
      },
    })
      .then((response) => {
        userProfile.value = response.data
        console.log(response.data)
      })
      .catch((error) => {
        console.log(error)
      })
})

</script>

<style scoped>

</style>