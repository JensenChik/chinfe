<style scoped>
    .layout{
        border: 1px solid #d7dde4;
        background: #f5f7f9;
    }
    .layout-logo{
        width: 100px;
        height: 30px;
        background: #5b6270;
        border-radius: 3px;
        float: left;
        position: relative;
        top: 15px;
        left: 20px;
    }
    .layout-nav{
        width: 600px;
        margin: 0 auto;
    }
    .layout-assistant{
        width: 300px;
        margin: 0 auto;
        height: inherit;
    }
    .layout-breadcrumb{
        padding: 10px 15px 0;
    }
    .layout-content{
        min-height: 200px;
        margin: 15px;
        overflow: hidden;
        background: #fff;
        border-radius: 4px;
    }
    .layout-content-main{
        padding: 10px;
    }
    .layout-copy{
        text-align: center;
        padding: 10px 0 20px;
        color: #9ea7b4;
    }
</style>
<template>
    <div class="layout">
        <Menu mode="horizontal" theme="dark" active-name="1">
            <Menu-item>conf space</Menu-item>
            <div class="layout-nav">
                <Menu-item name="1">
                    <Icon type="ios-navigate"></Icon>
                    任务调度
                </Menu-item>
                <Menu-item name="2">
                    <Icon type="ios-keypad"></Icon>
                    可视化平台
                </Menu-item>
                <Menu-item name="3">
                    <Icon type="ios-analytics"></Icon>
                    Hue
                </Menu-item>
                <Menu-item name="4">
                    <Icon type="ios-paper"></Icon>
                    Hadoop后台
                </Menu-item>
            </div>
        </Menu>
        <div class="layout-content">
            <Row>
                <i-col span="5">
                    <Menu active-name="1-1" width="auto" :open-names="['1']">
                        <Submenu name="1">
                            <template slot="title">
                                <Icon type="ios-navigate"></Icon>
                                任务管理
                            </template>
                            <Menu-item name="1-1">任务列表</Menu-item>
                            <Menu-item name="1-2">新建任务</Menu-item>
                            <Menu-item name="1-3">修改任务</Menu-item>
                        </Submenu>
                        <Submenu name="2">
                            <template slot="title">
                                <Icon type="ios-keypad"></Icon>
                                日志管理
                            </template>
                            <Menu-item name="2-1">执行日志</Menu-item>
                            <Menu-item name="2-2">任务实例</Menu-item>
                            <Menu-item name="2-3">操作日志</Menu-item>
                        </Submenu>
                        <Submenu name="3">
                            <template slot="title">
                                <Icon type="ios-analytics"></Icon>
                                用户管理
                            </template>
                            <Menu-item name="3-1">用户列表</Menu-item>
                            <Menu-item name="3-2">新建用户</Menu-item>
                            <Menu-item name="3-3">修改用户</Menu-item>
                        </Submenu>
                        <Submenu name="4">
                            <template slot="title">
                                <Icon type="ios-analytics"></Icon>
                                机器管理
                            </template>
                            <Menu-item name="4-1">机器列表</Menu-item>
                            <Menu-item name="4-2">机器状态</Menu-item>
                            <Menu-item name="4-3">新增机器</Menu-item>
                            <Menu-item name="4-4">修改机器</Menu-item>
                        </Submenu>

                    </Menu>
                </i-col>
                <i-col span="19">
                    <div id="table" class="layout-content-main">内容区域</div>
                    <test></test>
                </i-col>
            </Row>
        </div>
        <div class="layout-copy">
            2011-2016 &copy; conj.space
        </div>
    </div>
</template>
<script>
    module.exports = {
        components : {
            'test' : require('./task_table.vue')
        }
    }
</script>
