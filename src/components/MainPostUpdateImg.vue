<template>
  <div :class="`upload-image ${filter}`" :style="{ 'background-image': `url(${uploadImg})` }"></div>
  <div class="filters">
    <div v-for="(a) in filterList" :key="a" :class="`filter-item ${a}`" :style="{ 'background-image': `url(${uploadImg})` }" @click="$emit('filterSelect',a)"></div>
  </div>
</template>

<script>
export default {
    data(){
        return{
            filterList : [ "aden", "_1977", "brannan", "brooklyn", "clarendon", "earlybird", "gingham", "hudson", 
                        "inkwell", "kelvin", "lark", "lofi", "maven", "mayfair", "moon", "nashville", "perpetua", 
                        "reyes", "rise", "slumber", "stinson", "toaster", "valencia", "walden", "willow", "xpro2"]
        }
    },
    props:{
        uploadImg:String,
        filter:String,

    }
}
</script>

<style>

.filters{
    overflow-x:scroll;
    white-space: nowrap;
}
.filter-item {
  width: 100px;
  height: 100px;
  margin: 10px 10px 10px auto;
  padding: 8px;
  display: inline-block;
  color : white;
  background-size: cover;
  background-position : center;
}
.upload-image{
    width: 100%;
    height: 400px;
  background-size: contain;
  background-position: center;
  background-repeat: no-repeat;
}
</style>