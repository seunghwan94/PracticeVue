import { createStore } from 'vuex'
import axios from 'axios'

const store = createStore({
    state() {
        return {
            name : 'LEE',
            age : 20,
            likes : 30,
            more: {},
        }
    },
    mutations: {
        nameChange(state){
            state.name = 'Pack'
        },
        ageChange(state, payload){
            state.age = state.age+payload;
        },
        likesChange(state, data){
            if (data){
                state.likes++;
            }else{
                state.likes--;
            }
            
        },
        setMore(state, data){
            state.more = data
        },
    },
    actions: {
        getData(){
            axios.get('http://127.0.0.1:5000/api/post')
            .then(response =>{
              console.log(response.data);
              this.commit('setMore',response.data)
            })
            .catch(e=>{
              console.error('에러남',e);
            })
        }
    },

})

export default store;