    <!-- Bootstrap core JavaScript -->
      <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

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
