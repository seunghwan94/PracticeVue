<template>

  <div class="total-header">
    <div v-if="is_main==1" @click="is_main--">Cancle</div>
    <div v-else></div>
    <div><img alt="Vue logo" src="./assets/img/logo.png"></div>
    <div v-if="is_main==1" @click="is_main++">Next</div>
    <div v-if="is_main==2" @click="publish">발행</div>
    <div v-if="is_main==0"></div>
  </div>

  <div class="total-body" v-if="is_main==0">
    <MainContainVue :postList="postListData" @more="more()"/>
  </div>
  <div class="total-body" v-if="is_main==1">
    <MainPostUpdateImgVue :uploadImg="uploadImg" @filterSelect="filterSelect" :filter="filter"/>
  </div>
  <div class="total-body" v-if="is_main==2">
    <MainPostUpdateTextVue :uploadImg="uploadImg" @write="write = $event" :filter="filter"/>
  </div>

  <div class="total-footer">
    <div></div>
    <div>      
      <label for="file" class="file-upload-label" style="font-size: 35px;">+</label>
      <input @change="upload" type="file" id="file" class="file-input" />
    </div>
    <div></div>
  </div>
  
</template>

<script>
import MainContainVue from './components/MainContainView.vue';
import MainPostUpdateImgVue from './components/MainPostUpdateImg.vue';
import MainPostUpdateTextVue from './components/MainPostUpdateText.vue';

import postListData from './assets/data/postList.js';
import axios  from 'axios';



export default {
  name: 'App',
  data() {
    return {
      postListData:postListData,
      is_main: 0,
      uploadImg: '',
      write:'',
      filter: '' ,
    }
  },
  methods: {
    publish(){
      let publishData = {
        "profileImg": "3.jpg",
        "profileName": "test",
        "postImg": "3.jpg",
        "postMainTitle": "testttt",
        "postSubTitle": this.write,
        "postDate": "June 12, 2023"
      }
      this.postListData.unshift(publishData);
      this.is_main=0;
    },
    more(){
      axios.get('http://127.0.0.1:5000/api/post')
      .then(response =>{
        console.log(response.data);
        this.postListData.push(...response.data);
      })
      .catch(e=>{
        console.error('에러남',e);
      })
    },
    upload(e){
      let fileImg = e.target.files;
      let url = URL.createObjectURL(fileImg[0]);
      this.uploadImg = url;
      this.is_main++;
    },
    filterSelect(a){
      console.log(a);
      this.filter=a;
    }
  },
  components: {
    MainContainVue,
    MainPostUpdateImgVue,
    MainPostUpdateTextVue,
  }
}
</script>

<style>
body {
  margin:0px;
  padding: 0px;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: space-between;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 430px;
  height: 932px;
}

.total-header, .total-footer {
  width: 100%;
  height: 50px;
  background: rgb(130, 161, 133);
  display: flex;
  justify-content: space-between;
  align-items: center;
  /* padding: 5px 10px; */
}
.total-header div, .total-footer div{
  padding: 5px 10px;
  color: rgb(255, 255, 255);
  font-size: 17px;;
  cursor: pointer;
}

.total-header img {
  width: 30px;
}

.total-body {
  height: 832px;
}
.file-input {
  display: none;
}
</style>
