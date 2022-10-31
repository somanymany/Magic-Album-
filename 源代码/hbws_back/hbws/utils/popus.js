// 公用请求云函数
function list(ids, imgbase){
  return new Promise((resolve,reject)=>{
    let face = wx.cloud.callFunction({
      name:'face',
      data:{
        id: ids,
        image: imgbase
      }
    })
    resolve(face)
    reject(face)
  })
}

export {list}
