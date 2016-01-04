% include('header.tpl')
<br />
<br />
<div class="panel-group" id="accordion">
  <div class="panel panel-default">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion" href="#collapseOne">
          About
        </a>
      </h4>
    </div>
    <div id="collapseOne" class="panel-collapse collapse in">
      <div class="panel-body">
    <div class="row featurette featureImagePad">
            <div class="col-sm-6 col-md-5">
              <img class="featurette-image img-responsive img-circle"  src="/images/{{main_pic}}">
            </div>
            <div class="col-sm-6 col-md-7 featureTextPad">
            % if len(name) > 13:
                  <h3 class="featurette-heading"><span class="text-muted">Hi, I'm</span> {{name}}.</h3>
            % else:
                  <h2 class="featurette-heading"><span class="text-muted">Hi, I'm</span> {{name}}.</h2>
            % end 
              <p class="lead">{{header_quotation}}</p>
            </div>
          </div>
    </div>
      </div>
    </div>
  </div>
  <div class="panel panel-default">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion" href="#collapseTwo">
          Resume and GitHub
        </a>
      </h4>
    </div>
    <div id="collapseTwo" class="panel-collapse collapse">
      <div class="panel-body">
        <div class="row padMe">
          <div class="col-md-6">
            <div class="row">
              <div class="col-xs-12 col-sm-6 col-md-6 imageLower">
                <img src="/images/docs.png">
              </div>
              <div class="col-xs-12 col-sm-5 col-md-6 buttonLower">
                <div class="btn-group">
                  <a target="_blank" href="{{gdoc_URL}}" class="col-xs-9 col-sm-9 col-md-9 btn btn-primary btn-lg" role="button" data-toggle="tooltip" data-placement="bottom" title="Go to Google doc, or download directly">Resume</a>
                  <button type="button" class="col-xs-3 col-sm-3 col-md-3 btn btn-primary btn-lg dropdown-toggle" data-toggle="dropdown">
                    <span class="caret"></span>
                    <span class="sr-only">Toggle Dropdown</span>
                  </button>
                  <ul class="dropdown-menu" role="menu">
                    <li><a href="{{resume_pdf_download_URL}}">Download .PDF</a></li>
                    <li class="divider"></li>
                    <li><a href="{{resume_docx_download_URL}}">Download .Docx</a></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="row">
              <div class="col-xs-12 col-sm-6 col-md-6">
                <img src="/images/githubcat.png">
              </div>
              <div class="col-xs-12 col-sm-6 col-sm-5 col-md-6 buttonLower">
                <a target="_blank" href="{{GitHub_URL}}" class="btn btn-primary btn-lg" role="button" data-toggle="tooltip" data-placement="bottom" title="Check out my GitHub">GitHub</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
% if optional_panel:
       <div class="panel panel-default">
          <div class="panel-heading">
            <h4 class="panel-title">
              <a data-toggle="collapse" data-parent="#accordion" href="#collapseThree">
                {{optional_panel_title}}
              </a>
            </h4>
          </div>
          <div id="collapseThree" class="panel-collapse collapse">
            <div class="panel-body">
              <h2>
                <p>
                  <img src="/images/{{optional_panel_pic}}">
                  <a target="_blank" href="{{optional_panel_button_URL}}" class="btn btn-primary btn-lg" role="button">{{optional_panel_button_text}}</a>
                </p>
              </h2>
            </div>
          </div>
       </div> 
      </div>
% end
% include('footer.tpl')
