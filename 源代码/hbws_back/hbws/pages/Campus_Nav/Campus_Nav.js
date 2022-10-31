// pages/faceing/faceing.js
var {log} = console
var app = getApp()
Page({
  data: {
      theme:true,
      num:'',
      ids:'',
      aibase:'',
      saveToDiskFile:"",
  },
//onload
onLoad:function(options){
    var that = this
    const aiimg = options.aiimg
    app.globalData.imageToDisk = aiimg

    wx.request({
      //url: 'http://127.0.0.1:8000/api/NothingView/',
      url:'http://124.222.26.209:8000/api/NothingView/',
      method:'POST',
      header: {
        'content-type': 'application/json' 
      },
      success(res){
        console.log(res.data)
        that.setData({
          img_get:aiimg
        }),
        wx.showToast({
          title: '魔法生成结束',
        })
      },
      fail(res){
          console.log(res.errMsg)
      }
    }),
    log('开始测试保存文件功能')
  },
  saveToDisk(){
    log("成功点击下载按钮")
    wx.showLoading({
      title:"正在拉取图片"
    })
    wx.getImageInfo({
      src: app.globalData.imageToDisk,
      success(res){
        wx.hideLoading({
        })
        log(res)
        wx.saveImageToPhotosAlbum({
          filePath: res.path,
          success(res){
              log('保存成功')
              wx.showToast({
                title: '成功保存到相册',
                duration:1000
              })
          }
        })
        wx.showToast({
          title: '成功保存到相册',
          duration:1000})
      },
      fail(res){
          log(res.errMsg)
      }
    })
 },

 //tab切换
 character(event){
   log('现在测试是否能拿到ID值')
   log(event)
   let anara = event.currentTarget.dataset.index
   log(anara)
   let ids = event.currentTarget.id
   this.setData({
     num:anara,
     ids:ids
   })
   this.shadow()
   wx.showLoading({
     title: '转换生成中',
   })
   this.aiFuch(ids)
 },

 theMe(){
   this.setData({
     theme:false
   })
 },
 //隐藏
 shadow(){
  this.setData({
    theme:true
  })
},
})