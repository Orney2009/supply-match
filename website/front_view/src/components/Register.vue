<template>
  <section class="bg-gray-50 min-h-screen flex items-center justify-center">
    <div class="w-full max-w-md px-6 py-8 mx-auto">

      <router-link to="/" class="flex justify-center mb-6 text-2xl font-semibold text-blue-600" >
        SUPPLY MATCH
      </router-link>

     
      <div class="bg-white rounded-lg shadow p-6 sm:p-8">
        <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl mb-6">
          Créer votre compte
        </h1>

        <div class="flex justify-center text-red-600 mb-5">
          <span> {{ result }}</span>
        </div>

        <form class="space-y-4" @submit.prevent="handleSubmit">          
          <div>
            <label class="block mb-2 text-sm font-medium text-gray-900">
              Votre email
            </label>
            <input  type="email" placeholder="johndoe@gmail.com" v-model="email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg  focus:ring-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" required/>
          </div>


          <div> 
            <label class="block mb-2 text-sm font-medium text-gray-900">
              Mot de passe
            </label>
            <input type="password" v-model="password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"  required/>
          </div>

        
          <div>
            <label class="block mb-2 text-sm font-medium text-gray-900">
              Confirmez le mot de passe
            </label>
            <input  type="password" v-model="c_password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" required/>
          </div>

         
          <button type="submit" class="w-full text-white bg-blue-600 hover:bg-blue-700 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center transition" >
            Création de compte
          </button>

          <p class="text-sm text-gray-500 text-center">
            Avez-vous déjà un compte ?
            <router-link to="/login" class="font-medium text-blue-600 hover:underline" >
              Connexion
            </router-link>
          </p>
        </form>
      </div>
    </div>
  </section>
</template>

<script >
  import axios from 'axios';

  export default{
    name: 'Register',
    data(){
      return {
        email:'',
        password:'',
        c_password:'',
        result: ''
      }
    },
    methods: {
      async handleSubmit(){

        try {                    
          const response = await axios.post ('register',{
          email :this.email,
          password : this.password,
          c_password:  this.c_password
          })
          
          if (response.status == 201){                        
            this.$router.push("/")
          }          
          
        } catch (error) {          
          this.result = error.response.data.response
        }
                
      }
    },
  }

</script>