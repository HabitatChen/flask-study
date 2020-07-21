;
var login_ops = {
    init: function() {
        this.eventBind()
    },
    eventBind: function() {
        $('.login-wrap .login-btn').click(function() {
            var btn_target = $(this)

            if ( btn_target.hasClass('disabled') ) {
                alert('正在处理 请不要重复点击')
            }

            var login_name = $('.login-wrap input[name=login_name]').val()
            var login_pwd = $('.login-wrap input[name=login_pwd]').val()
            console.log(login_name, login_pwd)

            // 前端进行校验
            if (login_name === undefined || login_name.length < 1) {
                alert('用户名格式不正确')
                return
            }

            if (login_pwd === undefined || login_pwd.length < 6) {
                alert('密码格式不正确')
                return
            }

             btn_target.addClass('disabled')

            $.ajax({
                url: '/member/login',
                type: 'POST',
                data: {
                    login_name,
                    login_pwd
                },
                dataType: 'json',
                success: function( res ) {
                    console.log('res', res)
                    btn_target.remove('disabled')
                    if (res.status === 1) {
                        window.location.href = '/'
                    }
                }
            })
        })
    }
}

$(document).ready(function() {
    login_ops.init()
})

