<!-- HTML -->
<template>
	<div class="container">
		<div class="inner-container">
			<div id="wrapper">
				<h1 id="title">LET'S<br />SCHED<br />IT.</h1>
				<h2 id="message">Login to create and sched<br />a new event!</h2>
	
				<div class="login-button" @click="login">
					<div style="height:50px;width:240px;" class="abcRioButton abcRioButtonBlue">
						<div class="abcRioButtonContentWrapper">
							<div class="abcRioButtonIcon" style="padding:15px">
								<div style="width:18px;height:18px;">
									<img src="//developers.google.com/identity/images/g-logo.png" width="18px" height="18px">
								</div>
							</div>

							<span style="font-size:16px;line-height:48px;" class="abcRioButtonContents">
								<span>Sign in with Google</span>
							</span>
						</div>
					</div>
				</div>
			</div>
	
			<div id="footer">
				<h3>Built with 💖 by Oliners.</h3>
			</div>
		</div>
	</div>
</template>


<!-- CSS -->
<style scoped>
.container {
	background-image: url("../assets/leaves.jpg");
	background-size: cover;
	background-position: right;
	background-repeat: no-repeat;
	height: 100%;
}

.inner-container {
	width: min-content;
	height: 100%;
	display: flex;
	flex-direction: column;
	padding-left: 2rem;
	padding-right: 18rem;
	background: white;
}

#wrapper {
	flex: 1 0 auto;
}

#title {
	line-height: 7rem;
	margin: 4rem 1rem 0 0;
}

#message {
	font-size: 1.75rem;
	margin-left: 0;
}

.login-button {
	margin: 2rem 0;
}

.abcRioButton{
	border-radius:1px;
  box-shadow:0 2px 4px 0 rgba(0,0,0,.25);
  box-sizing:border-box;
  transition:background-color .218s,border-color .218s,box-shadow .218s;
  background-color:#fff;
  background-image:none;
  color:#262626;
  cursor:pointer;
  outline:none;
  overflow:hidden;
  position:relative;
  text-align:center;
  vertical-align:middle;
  white-space:nowrap;
  width:auto
}

.abcRioButton:hover{
  box-shadow:0 0 3px 3px rgba(66,133,244,.3)
}

.abcRioButtonBlue{
  background-color:#4285f4;
  border:none;
  color:#fff
}

.abcRioButtonBlue:hover{
  background-color:#4285f4
}

.abcRioButtonBlue:active{
  background-color:#3367d6
}

.abcRioButtonIcon{
  float:left
}

.abcRioButtonBlue .abcRioButtonIcon{
  background-color:#fff;
	border-radius:1px
}

.abcRioButtonContents{
  letter-spacing:.21px;
  margin-left:6px;
  margin-right:6px;
  vertical-align:top;
	font-weight: 500;
}

.abcRioButtonContentWrapper{
  height:100%;
  width:100%
}

.abcRioButtonBlue .abcRioButtonContentWrapper{
  border:1px solid transparent
}

#footer {
	border-top: black solid 1px;
	width: 20rem;
	flex-shrink: 0;
	margin: 2rem 0;
}
</style>


<!-- JAVASCRIPT -->
<script>
export default {
  name: 'CreateLogin',
	components: { },
	data() {
    return { }
  },
  props: {
    uuid: String,
	},
  methods: {
    login() {
			this.$getGapiClient().then(gapi => gapi.auth2.getAuthInstance().signIn().then(() => {
				console.log('Welcome to the future,', this.$getUserData().firstName)
				this.$router.push('create-event');
			}));
    },
    getcal() {
      var date = new Date();
      date.setDate(date.getDate() + 7);

      this.$getGapiClient().then(gapi => { 
        gapi.client.calendar.freebusy.query({
          'timeMin': (new Date()).toISOString(),
          'timeMax': (date.toISOString()),
          "items": [{ "id": 'primary' }]
        })
			});
    }
  }}
</script>
