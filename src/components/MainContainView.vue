<template>
    <div class="main-contain">
        <MainPostViewVue />
        <MainPostViewVue />
    </div>

</template>

<script>
import MainPostViewVue from './MainPostView.vue'

export default {
    components:{
        MainPostViewVue
    }
}
</script>

<style>
.main-contain {
    width: 100%;
    height: 100%; /* 원하는 높이로 설정 */
    overflow: auto; /* 내용이 넘칠 경우 스크롤 가능하게 설정 */
    border: 1px solid #ccc; /* 컨테이너 경계를 시각적으로 확인하기 위해 */
}
</style>