// pages/faceing/faceing.js
var {log} = console
var app = getApp()
Page({
  data: {
      theme:true,
      num:'',
      ids:'',
      aibase:'',
      imagePath:'',
  },
//onload
onLoad:function(options){
    var that = this
    const aiimg = options.base64ImgUrl
    app.globalData.imageToDisk = options.base642Image
    wx.request({
      url: 'http://124.222.26.209:8000/api/NothingView/',
      method:'POST',
      header: {
        'content-type': 'application/json' 
      },
      success(res){
        that.setData({
          img_get:aiimg
        })
        wx.showToast({
          title: '魔法生成结束',
        })
      },
      fail(res){
          console.log(res.errMsg)
      }
    })
  },
  saveToDisk(){
    app.globalData.imageIndex = Math.round(Math.random()*10000)
    const fs = wx.getFileSystemManager()
    const Imgpath = wx.env.USER_DATA_PATH + '/base64img' + app.globalData.imageIndex + '.jpg'
    console.log(Imgpath)
    fs.writeFile({
        filePath: Imgpath,  // 要写入的文件路径 (本地路径)
        data: app.globalData.imageToDisk,  // base64图片, 此处图片src不能有 data:image/jpeg;base64, 前缀
        encoding: 'base64',
        success(res) {
            wx.saveImageToPhotosAlbum({
                filePath: Imgpath,  // 要写入的文件路径 (本地路径)
                success: function (res) {
                    console.log(res)
                    log('保存成功')
                },
                fail: function (err) {
                    console.log(err)
                },
                complete: function () {
                    //删除临时文件
                    var fileManager = wx.getFileSystemManager(); //全局唯一的文件管理器
                    fileManager.unlink({ //删除
                        filePath: wx.env.USER_DATA_PATH + '/base64img' + '.jpg',
                        success: function (resf) {
                            console.log('unlink', resf)
                            wx.showToast({
                              title: '成功保存到相册',
                              duration:1000})
                        }
                    })
                }
            }),
            wx.showToast({
              title: '成功保存到相册',
              duration:1000})
      },
      fail(res){
        console.error(res)
      }
    })   
 },
 //tab切换
 character(event){


   let anara = event.currentTarget.dataset.index

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