//index.js
var {log} = console
// 引入公用函数
import {list} from '../../utils/popus.js'

Page({
  data: {
    imgUrls: [
      'https://zhenz-1309499835.cos.ap-beijing.myqcloud.com/hbws/images/1-1.jpg',
      'https://zhenz-1309499835.cos.ap-beijing.myqcloud.com/hbws/images/1-2.jpg',
      'https://zhenz-1309499835.cos.ap-beijing.myqcloud.com/hbws%2Fimages%2F1-3.jpg'
    ],
    swiperIndex: 0
  },
  // 轮播特效果一
  swiperChange(e) {
    this.setData({
      swiperIndex: e.detail.current
    })
  },
  // 选择图片
  faceImage(event){
    var that = this;
    console.log('选择图片功能')
    wx.chooseMedia({
      count: 9,
      mediaType: ['image','video'],
      sourceType: ['album', 'camera'],
      success(res) {
        wx.showLoading({
          title: '魔法生成中',
        })
        const tempFilePaths = res.tempFiles
        const img_src = tempFilePaths[0].tempFilePath
        const img_size = tempFilePaths[0].size
        const imgbase = wx.getFileSystemManager().readFileSync(tempFilePaths[0].tempFilePath,"base64")//转码为base64
        let base64url = null
        log('正在测试上传前')
        wx.request({
          //url: 'http://127.0.0.1:8000/api/Campus_Graduation/',
          url: 'http://124.222.26.209:8000/api/Campus_Graduation/',
          method:'POST',
          data:{
            myImage:imgbase
          },
          header: {
            'content-type': 'application/json' 
          },
          success(res){
            wx.hideLoading({
            })
            log("正在测试服务器上传")
            var aiimg = res.data.Image
            wx.navigateTo({
              //这里url的变量名称不要随意修改
              url: '../Campus_Nav/Campus_Nav?aiimg='+ aiimg 
            })
          },
          fail(res){
            console.log(res.errMsg)
          }
        })
      }
    })
  }
})