<style scoped>
    .expand-row{
        margin-bottom: 24px;
    }
</style>
<template>
    <div>
        <Row class="expand-row">
            <Col span="5">
            <span class="expand-key">创建者：</span>
            <span class="expand-value">{{ row.user }}</span>
            </Col>
            <Col span="5">
            <span class="expand-key">创建时间：</span>
            <span class="expand-value">{{ row.create_time }}</span>
            </Col>
            <Col span="5">
            <span class="expand-key">优先级：</span>
            <span class="expand-value">{{ row.priority }}</span>
            </Col>
            <Col span="4">
            <span class="expand-key">失败重跑：</span>
            <span class="expand-value">{{ row.rerun }}</span>
            </Col>
            <Col span="5">
            <span class="expand-key">重跑次数：</span>
            <span class="expand-value">{{ row.rerun_times }}</span>
            </Col>
        </Row>
        <Row class="expand-row">
            <Col span="24">
            <span class="expand-key">执行命令：</span>
            <span class="expand-value">{{ row.command }}</span>
            </Col>
        </Row>
        <Row class="expand-row">
            <Col span="24">
            <span class="expand-key">机器池：</span>
            <span class="expand-value">{{ row.machine_pool }}</span>
            </Col>
        </Row>
        <Row class="expand-row">
            <Col span="24">
            <span class="expand-key">父任务：</span>
            <span class="expand-value">{{ row.father_task }}</span>
            </Col>
        </Row>
        <Row>
            <Col span="24">
            <span class="expand-key">子任务：</span>
            <span class="expand-value">{{ row.child_task }}</span>
            </Col>
        </Row>
        </Row>
    </div>
</template>
<script>
    export default {
        props: {
            row: Object
        }
    };
</script>