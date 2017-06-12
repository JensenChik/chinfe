<template>
    <Table height="800" :columns="columns10" :data="data9"></Table>
</template>
<script>
    import expandRow from './task-table-expand.vue';
    export default {
        components: { expandRow },
        data () {
            return {
                columns10: [
                    {
                        type: 'expand',
                        width: 50,
                        render: (h, params) => {
                        return h(expandRow, {
                            props: {
                                row: params.row
                            }
                        })
                    }
            },
            {
                title: '任务ID',
                key: 'task_id'
            },
            {
                title: '是否启用',
                key: 'valid'
            },
            {
                title: '任务名',
                key: 'task_name'
            },
            {
                title: '调度格式',
                key: 'scheduled'
            },
            {
                title: '操作',
                key: 'action'
            }
        ],
            data9: [
                {
                    task_id: '18',
                    valid: true,
                    task_name: '【爬虫】京东内存数据',
                    scheduled: 'D 01:10',
                    action: '查看日志|紧急操作',
                    user:'chin'
                },
                {
                    task_id: '17',
                    valid: true,
                    task_name: '【数据仓库source】魔兽世界拍卖行sqoop同步',
                    scheduled: 'D  04:00',
                    action: '查看日志|紧急操作',
                    user:'chin'
                },
                {
                    task_id: '16',
                    valid: true,
                    task_name: '【爬虫】魔兽世界拍卖行数据',
                    scheduled: 'D  04:00',
                    action: '查看日志|紧急操作',
                    user:'chin'
                },
                {
                    task_id: '15',
                    valid: true,
                    task_name: '【数据仓库source】京东数据sqoop同步',
                    scheduled: 'D  03:00',
                    action: '查看日志|紧急操作',
                    user:'chin'
                }
            ]
        }
        }
    }
</script>
