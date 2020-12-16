<template>
    <div class="fillcontain">
        <el-button @click="aaa" style="margin-bottom: 10px" type="success">{{ button }}</el-button>
        <el-button @click="bbb" style="margin-bottom: 10px" type="success">传送信息！</el-button>
        <div class="contain">
            <vue-command
                class="vuecommand"
                ref="aa" title="高级计算机网络大作业"
                prompt="NjuSofware@ctl:#"
                :history.sync="history"
                :commands="commands"
                :is-in-progress="true">
            </vue-command>
        </div>
    </div>
</template>

<script>
import VueCommand, { createStdout } from 'vue-command';
import 'vue-command/dist/vue-command.css';


export default {
    name: 'Command',
    components: {
        VueCommand
    },
    created() {


    },
    mounted() {
        console.log(this.$refs.aa);
        let stdins = this.$refs.aa.$refs.stdin;
        this.stdins = stdins
        this.lastStdin = this.stdins[this.stdins.length - 1];
        this.stdinsLen = this.stdins.length
    },
    data: () => ({
        commands: {
            'hello': () => {
                createStdout('Hello world ');
            },
            'echo': _ => createStdout(JSON.stringify(_, null, 2)),
            'echo1': _ => createStdout(JSON.stringify(_, null, 2)),
            'echo2': _ => createStdout('JSON.stringify(_, null, 2)')


        },
        button: 'send two messages',
        remoteStr: '',
        history: [],
        lastStdin: null,
        stdinsLen: 0,
        stdins: null

    }),
    methods: {
        aaa() {

            // let flag = true;
            // this.sleep(5).then(res=>{
            //     lastStdin.local.stdin = new String("echo a");
            //     lastStdin.handle();
            //     return this.sleep(300)
            // }).then(res=>{
            //     lastStdin = stdins[stdins.length - 1];
            //     lastStdin.local.stdin = new String("echo b");
            //     lastStdin.handle();
            //     return this.sleep(300)
            // })

            this.lastStdin.local.stdin = new String("echo a");
            this.handle()
            this.lastStdin.local.stdin = new String("echo b");
            this.handle();

        },
        handle(){
            // while (this.stdinsLen != )
            this.lastStdin.handle()
        },

        bbb() {
            this.history.push(createStdout('你坏<br>哈哈'));
            this.history.push(createStdout('你好'));
        },
        sleep(time) {
            return new Promise((resolve) => setTimeout(resolve, time));
        }
    }
};
</script>

<style scoped>
.fillcontain {
    background: #fff;
    padding: 20px 20px;

}

.contain {
    height: 420px;
}

.vuecommand {
    min-height: 400px;
    max-height: 400px;
    overflow-y: scroll;
}
</style>