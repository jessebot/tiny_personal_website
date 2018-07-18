    <!-- Bootstrap core JavaScript -->
    <script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>
    <script>
        $(function () {
          $('[data-toggle="tooltip"]').tooltip()
          });
        $(document).ready(function() {
            $("div.list-group>a").click(function(e) {
                e.preventDefault();
                $(this).siblings('a.active').removeClass("active");
                $(this).addClass("active");
                var HalfUnit = $(this).parent().parent().parent()
                var tabChildren = HalfUnit.children("div.bhoechie-tab").children("div.bhoechie-tab-content");
                var tabChildrenActive = HalfUnit.children("div.bhoechie-tab").children("div.bhoechie-tab-content.active");
                var index = $(this).index()
                $(tabChildren).eq(index).addClass("active");
                $(tabChildrenActive).removeClass("active");
              });
          });
          $('#mainTabs a').click(function (e) {
            e.preventDefault()
            $(this).tab('show')
           });
    </script>
  </body>
</html>
