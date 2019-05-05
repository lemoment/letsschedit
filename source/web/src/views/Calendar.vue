<template>
    <div id="cal">
        <full-calendar :events="events"></full-calendar>
    </div>
</template>

<script>
import 'fullcalendar/dist/fullcalendar.css'

export default {
    name: 'Calendar',
    data() {
        return {
            events: [
                {
                    title  : 'event1',
                    start  : '2019-05-04',
                },
                {
                    title  : 'event2',
                    start  : '2010-01-05',
                    end    : '2010-01-07',
                },
                {
                    title  : 'event3',
                    start  : '2010-01-09T12:30:00',
                    allDay : false,
                },
            ]
        }
    }
}
</script>

<style scoped>
</style>