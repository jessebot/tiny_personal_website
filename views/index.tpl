% include('header_main.tpl')
    <div class="container">
      <div class="row">
          <div class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
            <div class="dash-unit bhoechie-tab-container">
              <dtitle>
                  <span aria-hidden="true" class="li_user fs1"></span>
              {{globals['name']}}</dtitle>
              <hr style="margin-bottom: 0;">
        <img class="img-responsive img-rounded center-block main-img"
             src="/images/{{globals['image']}}"
             alt="What I look like."
             style="width:250px;"
             data-toggle="tooltip" data-placement="bottom"
             title="{{globals['name']}}">
            </div><!-- /.dash-unit -->
          </div><!-- /.col -->
        <div class="col-xs-9 col-sm-7 col-md-8 col-lg-8 col-xl-8">
          <div class="dash-unit bhoechie-tab-container">
            <ul class="nav nav-tabs" role="tablist">
              <li role="presentation" class="col-lg-4 col-md-4 col-sm-4 col-xs-4 col-xl-4 active">
                <a href="#resume" aria-control="resume" role="tab" data-toggle="tab" aria-expanded="true">
                  <img src="/images/googledocs.svg" style="width: 64px;">
                </a>
                </li>
              <li role="presentation" class="col-lg-4 col-md-4 col-sm-4 col-xs-4">
                <a href="#linkedin" aria-control="linkedin" role="tab" data-toggle="tab" aria-expanded="false">
                  <img src="/images/linkedin.svg" style="width: 64px;">
                </a>
              </li>
              <li role="presentation" class="col-lg-4 col-md-4 col-sm-4 col-xs-4 col-xl-6">
                <a href="#github" aria-control="github" role="tab" data-toggle="tab" aria-expanded="false">
                  <img src="/images/github-cat.svg" style="width: 64px;">
                </a>
              </li>
            </ul>
            <div class="tab-content">
              <!-- Steam -->
              <div role="tabpanel" class="tab-pane active" id="resume">

              <center>
                  <dtitle>
                  <span aria-hidden="true" class="li_note fs1"></span>
                  resume</dtitle>
                  <hr>
                    <h7>
                      <span aria-hidden="true" class="li_clip fs1"></span>
                      Download: <a href="{{globals['resume_pdf_URL']}}">PDF</a> or <a href="{{globals['resume_docx_URL']}}">Word Doc</a>
                      <br />
                      <br />
                      <span aria-hidden="true" class="li_world fs1"></span>
                      Go to <a target="_blank" href="{{globals['resume_live_doc_URL']}}">Google Doc</a>
                    </h7>
              </center>
              </div><!-- tab panel-->
              <!-- Linkedin -->
              <div role="tabpanel" class="tab-pane" id="linkedin">
              <center>
                <dtitle>
                      <span aria-hidden="true" class="li_world fs1"></span>
                linkedin</dtitle>
                <hr>
                  <h7>
                      <span aria-hidden="true" class="li_user fs1"></span>
                        <a target="_blank" href="{{globals['linkedin_URL']}}"
                           role="button" data-toggle="tooltip" data-placement="left"
                           title="Linkedin" style="box-shadow: none;">
                          LinkedIn Profile
                        </a>
                  </h7>
              </center>
             </div><!-- tab panel-->
             <!-- Github section -->
             <div role="tabpanel" class="tab-pane" id="github">
               <center>
                 <dtitle>
                      <span aria-hidden="true" class="li_world fs1"></span>
                 github</dtitle>
                 <hr>
                   <h7>
                     <span aria-hidden="true" class="li_user fs1"></span>
                        <a target="_blank" href="https://github.com/{{globals['github_username']}}"
                           role="button" data-toggle="tooltip" data-placement="right"
                           title="GitHub" style="box-shadow: none;">
                           {{globals['github_username']}}
                        </a>
                   </h7>
               </center>
             </div><!-- tab panel-->
          </div><!-- tab-content -->
        </div><!-- /.dash-unit -->
        </div><!-- /.col -->
          <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-xs-12">
            <div class="dash-unit bhoechie-tab-container">
              <dtitle>
                  <span aria-hidden="true" class="li_star fs1"></span>
                About
              </dtitle>
              <hr>
            <div class="aboutText">
              {{globals['profile_blurb']}}
            </div>
            </div><!-- /.dash-unit -->
          </div><!-- /.col -->


      </div><!-- /.row ALL CARDS-->
    </div><!-- /.container MAIN-->

% include('footer_main.tpl')
