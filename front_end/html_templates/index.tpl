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
    <div class="row featurette">
            <div class="col-md-5 tinyPad">
              <img class="featurette-image img-responsive img-circle"  src="/images/{{main_pic}}">
            </div>
            <div class="col-md-7">
              <h2 class="featurette-heading"><br /><span class="text-muted">Hi, I'm</span> {{name}}.</h2>
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
          <div class="col-md-6 morePad">
            <img src="/images/docs.png">
              <div class="btn-group">
              <a href="{{gdoc_URL}}" class="btn btn-primary btn-lg">Resume</a>
              <button type="button" class="btn btn-primary btn-lg dropdown-toggle" data-toggle="dropdown">
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
          <div class="col-md-6">
              <p><img src="/images/githubcat.png"><a href="{{GitHub_URL}}" class="btn btn-primary btn-lg" role="button">GitHub</a></p>
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
              <h2><p><img src="/images/{{optional_panel_pic}}">       <a href="{{optional_panel_button_URL}}" class="btn btn-primary btn-lg" role="button">{{optional_panel_button_text}}</a></p></h2>
            </div>
          </div>
        </div> 
      </div>
% end
% include('footer.tpl')
