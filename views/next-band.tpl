% include('header_band.tpl')
    <div class="container">
      <div class="row">

          <!-- Input section -->
          <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-xs-12">
            <div class="dash-unit bhoechie-tab-container">
              <dtitle>
                  <span aria-hidden="true" class="li_star fs1"></span>
                The Name of My Next Band
              </dtitle>
              <hr>
              <center>
          <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-xs-12">
                <form action="/next-band" method="post">
                  <center>
                      <div class="form-row align-items-center">
                      <div class="col-md-5">
                          <img class="img-responsive img-rounded center-block main-img" src="/images/noun_rock_monster.png" alt="Band Monster >:3" style="height:250px;" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Band Monster">
                      </div>
                      <div class="form-group col-md-6">
                          Submit a band name, and it'll generate some cool art for you. Currently under construction.
                          <label for="inputBand" class="sr-only">Input Band Name Here</label>
                          <input type="text" class="form-control" id="inputBand" name="inputBand" placeholder="Band Name">
                          <button type="submit" class="btn btn-primary btn-sm mb-2">Submit</button>
                      </div>
                      </div>
                  </center>
                </form>
         </div>
              </center>
            </div> <!-- /.dash-unit -->
          </div> <!-- /.col -->

          <!-- Previous bands -->
          <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-xs-12">
            <div class="dash-unit bhoechie-tab-container">
              <dtitle>
                  <span aria-hidden="true" class="li_star fs1"></span>
                Previous Potential Band Names
              </dtitle>
              <hr>
              <center>
              <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-xs-12">
              % for band_set in bands:
                    <li>{{band_set[0]}}</li><br />
              % end
              </div>
              </center>
              
            </div><!-- /.dash-unit -->
          </div><!-- /.col -->

      </div><!-- /.row ALL CARDS-->
    </div><!-- /.container MAIN-->

% include('footer_main.tpl')
