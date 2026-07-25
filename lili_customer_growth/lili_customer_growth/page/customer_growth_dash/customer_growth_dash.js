frappe.pages['customer_growth_dash'].on_page_load = function(wrapper) {


    let page = frappe.ui.make_app_page({

        parent: wrapper,

        title: '智格科技新能源客户增长智能驾驶舱',

        single_column: true

    });



    // =========================
    // 页面背景
    // =========================

    $(page.body).css({

        background:"#020b18",

        padding:"20px",

        minHeight:"100vh"

    });



    // =========================
    // 科技风CSS
    // =========================

    $("<style>")
    .html(`


    .dashboard-title{

        text-align:center;

        color:#00eaff;

        font-size:36px;

        font-weight:bold;

        text-shadow:
        0 0 20px #00eaff;

        margin-bottom:10px;

    }



    .dashboard-subtitle{

        text-align:center;

        color:#9db3c7;

        margin-bottom:5px;

    }



    .dashboard-time{

        text-align:center;

        color:#00ffaa;

        margin-bottom:30px;

    }



    .tech-card{


        background:

        rgba(255,255,255,0.08);


        border:

        1px solid rgba(0,234,255,0.3);


        border-radius:20px;


        padding:20px;


        margin-bottom:20px;


        box-shadow:

        0 0 25px rgba(0,234,255,0.15);


        transition:.3s;


        animation:fadeIn .8s;


    }




    .tech-card:hover{


        transform:translateY(-5px);


        box-shadow:

        0 0 40px rgba(0,234,255,0.4);


    }




    @keyframes fadeIn{


        from{

            opacity:0;

            transform:translateY(30px);

        }


        to{

            opacity:1;

            transform:none;

        }


    }




    .kpi-title{


        color:#9db3c7;

        font-size:18px;


    }




    .kpi-number{


        color:#00eaff;

        font-size:48px;

        font-weight:bold;


        text-shadow:

        0 0 15px #00eaff;


    }




    .kpi-rate{


        color:#00ffaa;

        font-size:15px;


    }




    .chart-title{


        color:white;

        font-size:22px;

        font-weight:bold;

        margin-bottom:15px;


    }




    .insight{


        color:white;

        line-height:35px;


        background:

        rgba(0,255,170,.08);


        padding:20px;


        border-radius:15px;


        border-left:

        5px solid #00ffaa;


    }



    .status{


        text-align:center;

        color:#00ffaa;

        margin-top:20px;


    }



    `)
    .appendTo("head");





    // =========================
    // HTML
    // =========================


    $(page.body).html(`



<div class="dashboard-title">

⚡ 智格科技新能源客户增长智能驾驶舱

</div>




<div class="dashboard-subtitle">

New Energy Customer Growth Intelligence Cockpit

</div>




<div class="dashboard-time">

🟢 数据实时同步

<span id="update_time"></span>

</div>






<div class="row">



<div class="col-md-3">

<div class="tech-card text-center">


<div class="kpi-title">

累计客户

</div>


<div class="kpi-number"

id="total_customer">

0

</div>


<div class="kpi-rate">

客户资产规模

</div>


</div>

</div>





<div class="col-md-3">

<div class="tech-card text-center">


<div class="kpi-title">

活跃客户

</div>


<div class="kpi-number"

id="active_customer">

0

</div>


<div class="kpi-rate">

实时运营

</div>


</div>

</div>





<div class="col-md-3">

<div class="tech-card text-center">


<div class="kpi-title">

本月新增

</div>


<div class="kpi-number"

id="monthly_new">

0

</div>


<div class="kpi-rate">

增长动力

</div>


</div>

</div>





<div class="col-md-3">

<div class="tech-card text-center">


<div class="kpi-title">

流失客户

</div>


<div class="kpi-number"

id="lost_customer">

0

</div>


<div class="kpi-rate">

风险监控

</div>


</div>

</div>



</div>







<div class="tech-card">


<div class="chart-title">

📈 客户生命周期增长趋势

</div>


<div id="growth_chart"></div>


</div>







<div class="row">


<div class="col-md-6">


<div class="tech-card">


<div class="chart-title">

⚡ 服务类型分布

</div>


<div id="service_chart"></div>


</div>


</div>




<div class="col-md-6">


<div class="tech-card">


<div class="chart-title">

🌏 全国客户分布

</div>


<div id="city_chart"></div>


</div>


</div>


</div>







<div class="tech-card">


<div class="chart-title">

🔋 电池型号使用情况

</div>


<div id="battery_chart"></div>


</div>







<div class="tech-card">


<div class="chart-title">

🤖 智能运营洞察

</div>


<div class="insight"

id="ai_insight">

正在分析数据...

</div>


</div>







<div class="status">

SYSTEM ONLINE · NEW ENERGY DATA PLATFORM

</div>




`);
// ===============================
// 数字滚动动画
// ===============================


function animateNumber(id, target){


    let current = 0;


    let step = Math.ceil(target / 60);



    let timer = setInterval(function(){


        current += step;


        if(current >= target){


            current = target;


            clearInterval(timer);

        }


        $(id).text(current);



    },25);


}






// ===============================
// 更新时间
// ===============================


$("#update_time").text(

    new Date().toLocaleString()

);








// ===============================
// KPI数据
// ===============================


frappe.call({


    method:

    "lili_customer_growth.lili_customer_growth.page.customer_growth_dash.customer_growth_dash.get_dashboard_data",



    callback:function(r){


        let data=r.message;



        if(data){



            animateNumber(

                "#total_customer",

                data.total_customer

            );



            animateNumber(

                "#active_customer",

                data.active_customer

            );



            animateNumber(

                "#monthly_new",

                data.monthly_new

            );



            animateNumber(

                "#lost_customer",

                data.lost_customer

            );


        }


    }



});









// ===============================
// 客户增长趋势
// ===============================


frappe.call({


method:

"lili_customer_growth.lili_customer_growth.page.customer_growth_dash.customer_growth_dash.get_growth_trend",



callback:function(r){


    let data=r.message || [];



    new frappe.Chart("#growth_chart",{



        title:"客户增长趋势",



        data:{


            labels:data.map(

                d=>d.month

            ),



            datasets:[

            {

                name:"新增客户",

                values:data.map(

                    d=>d.total

                )

            }

            ]


        },



        type:"line",



        height:350


    });



}



});









// ===============================
// 服务类型分布
// ===============================


frappe.call({


method:

"lili_customer_growth.lili_customer_growth.page.customer_growth_dash.customer_growth_dash.get_service_type",



callback:function(r){


    let data=r.message || [];



    new frappe.Chart("#service_chart",{



        title:"服务类型占比",



        data:{



            labels:data.map(

                d=>d.service_type

            ),




            datasets:[

            {

                values:data.map(

                    d=>d.total

                )

            }

            ]



        },



        type:"donut",



        height:320


    });



}



});









// ===============================
// 全国客户分布
// ===============================


frappe.call({


method:

"lili_customer_growth.lili_customer_growth.page.customer_growth_dash.customer_growth_dash.get_city_distribution",



callback:function(r){



    let data=r.message || [];



    new frappe.Chart("#city_chart",{



        title:"全国客户分布",



        data:{



            labels:data.map(

                d=>d.city

            ),




            datasets:[

            {

                name:"客户数量",


                values:data.map(

                    d=>d.total

                )

            }

            ]



        },



        type:"bar",



        height:320



    });



}



});









// ===============================
// 电池型号分析
// ===============================


frappe.call({


method:

"lili_customer_growth.lili_customer_growth.page.customer_growth_dash.customer_growth_dash.get_battery_usage",



callback:function(r){



    let data=r.message || [];



    new frappe.Chart("#battery_chart",{



        title:"电池型号使用情况",



        data:{



            labels:data.map(

                d=>d.battery_model

            ),



            datasets:[

            {


                name:"使用数量",



                values:data.map(

                    d=>d.total

                )

            }

            ]



        },



        type:"bar",



        height:350



    });



}



});









// ===============================
// AI运营洞察
// ===============================


frappe.call({


method:

"lili_customer_growth.lili_customer_growth.page.customer_growth_dash.customer_growth_dash.get_dashboard_data",



callback:function(r){



    let data=r.message;



    if(data){


        $("#ai_insight")

        .html(`


        ✓ 当前累计服务客户：

        <b>${data.total_customer}</b> 家


        <br>


        ✓ 当前活跃客户：

        <b>${data.active_customer}</b> 家


        <br>


        ✓ 本月新增客户：

        <b>${data.monthly_new}</b> 家


        <br>


        ✓ 当前流失客户：

        <b>${data.lost_customer}</b> 家


        <br>


        ✓ 新能源客户运营状态：

        <b style="color:#00ffaa">

        正常

        </b>



        `);



    }



}



});



};