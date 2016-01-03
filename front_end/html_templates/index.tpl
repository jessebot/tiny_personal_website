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
              <img class="featurette-image img-responsive img-circle"  src="/images/defcon23.JPG">
            </div>
            <div class="col-md-7">
              <h2 class="featurette-heading"><br /><span class="text-muted">Hi, I'm</span> Jesse.</h2>
              <p class="lead">I'm a DevOps Engineer that loves Linux, the internet, and Python.</p>
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
              <a href="https://docs.google.com/document/d/1t-xBYBxyUbDKUKQFIY1_r0GnjCMIUAyelfnyIhTK2Uc/edit?pli=1" class="btn btn-primary btn-lg">Resume</a>
              <button type="button" class="btn btn-primary btn-lg dropdown-toggle" data-toggle="dropdown">
                <span class="caret"></span>
                <span class="sr-only">Toggle Dropdown</span>
              </button>
              <ul class="dropdown-menu" role="menu">
                <li><a href="https://docs.google.com/document/d/1t-xBYBxyUbDKUKQFIY1_r0GnjCMIUAyelfnyIhTK2Uc/export?format=pdf&id=1t-xBYBxyUbDKUKQFIY1_r0GnjCMIUAyelfnyIhTK2Uc">Download .PDF</a></li>
                <li class="divider"></li>
                <li><a href="https://docs.google.com/document/d/1t-xBYBxyUbDKUKQFIY1_r0GnjCMIUAyelfnyIhTK2Uc/export?format=docx&id=1t-xBYBxyUbDKUKQFIY1_r0GnjCMIUAyelfnyIhTK2Uc">Download .Docx</a></li>
              </ul>
              </div>
          </div>
          <div class="col-md-6">
              <p><img src="/images/githubcat.png"><a href="http://github.com/jessebot" class="btn btn-primary btn-lg" role="button">GitHub</a></p>
          </div>
      </div>
    </div>
    </div>
    </div>
 <div class="panel panel-default">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion" href="#collapseThree">
          Linux Newbie Class
        </a>
      </h4>
    </div>
    <div id="collapseThree" class="panel-collapse collapse">
      <div class="panel-body">
        <h2><p><img src="/images/penguin_copy.png">       <a href="http://howtonix.info" class="btn btn-primary btn-lg" role="button">How To *n?x</a></p></h2>
      </div>
    </div>
  </div> 
</div>
% include('footer.tpl')
