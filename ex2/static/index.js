superagent.get('/api/post').end((err, res) => {
  let data = res.body.result;
  jQuery($ => {
    $('#main').text(JSON.stringify(data));
  });
});

