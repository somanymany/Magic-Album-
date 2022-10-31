//index.js
var {log} = console
// 引入公用函数
import {list} from '../../utils/popus.js'

Page({
  data: {
    imgUrls: [
      'https://zhenz-1309499835.cos.ap-beijing.myqcloud.com/hbws%2Fimages%2F6-1.jpg',
      'https://zhenz-1309499835.cos.ap-beijing.myqcloud.com/hbws%2Fimages%2F6-2.jpg',
      'https://zhenz-1309499835.cos.ap-beijing.myqcloud.com/hbws%2Fimages%2F6-3.jpg'
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
        console.log(tempFilePaths)
        const img_src = tempFilePaths[0].tempFilePath
        const img_size = tempFilePaths[0].size
        const imgbase = wx.getFileSystemManager().readFileSync(tempFilePaths[0].tempFilePath,"base64")//转码为base64
        let base64url = null
        wx.uploadFile({
          filePath: img_src,
          name: 'myImage',
          url: 'http://124.222.26.209:8000/api/MiyazakiHayao_style/',
          method:'POST',
          header:{
            //'content-type':'application/x-www-form-urlencoded'
            'content-type':'application/form-data'
          },
          formData:{
            open_id : img_size
          },
          success(res){
            wx.hideLoading({
            })
            let base642Image = base64url
            base642Image = res.data
            base642Image = wx.arrayBufferToBase64(wx.base64ToArrayBuffer(base642Image))
            const base64ImgUrl = "data:image/png;base64," + base642Image
            wx.navigateTo({
              //这里url的变量名称不要随意修改
              url: '../Animation_Nav/Animation_Nav?base64ImgUrl='+ base64ImgUrl + '&base642Image=' + base642Image
            })
            that.setData({
              img_get:base64ImgUrl
            })
          },
          fail(res){
            console.log("上传失败",res.errMsg)
          }
        })
      }
    })
  }
})