import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { ROUTES } from './app.routes';
import { AlunoComponent } from './Aluno/Aluno-component';
import { AlunoItemComponent } from './Aluno/Aluno-item/Aluno-item.component';
import { AlunoService } from './Aluno/Aluno-service';
import { AlunoListComponent } from './Aluno/Aluno-list/Aluno-list.component';
import { NewAlunoComponent } from './Aluno/new-Aluno/new-Aluno.component';
import { ProfessorComponent } from './Professor/Professor-component';
import { ProfessorItemComponent } from './Professor/Professor-item/Professor-item.component';
import { ProfessorService } from './Professor/Professor-service';
import { ProfessorListComponent } from './Professor/Professor-list/Professor-list.component';
import { NewProfessorComponent } from './Professor/new-Professor/new-Professor.component';
import { CursoComponent } from './Curso/Curso-component';
import { CursoItemComponent } from './Curso/Curso-item/Curso-item.component';
import { CursoService } from './Curso/Curso-service';
import { CursoListComponent } from './Curso/Curso-list/Curso-list.component';
import { NewCursoComponent } from './Curso/new-Curso/new-Curso.component';
import { AulaComponent } from './Aula/Aula-component';
import { AulaItemComponent } from './Aula/Aula-item/Aula-item.component';
import { AulaService } from './Aula/Aula-service';
import { AulaListComponent } from './Aula/Aula-list/Aula-list.component';
import { NewAulaComponent } from './Aula/new-Aula/new-Aula.component';

import { NavigatorComponent } from './shared/navigator/navigator.component';
import { SearchBarComponent } from './shared/search-bar/search-bar.component';
import { DeleteButtonComponent } from './shared/delete-button/delete-button.component';
import { AuthService } from './shared/auth-service'
import { HeaderComponent } from './header/header.component'

@NgModule({
  declarations: [
    AppComponent,
    AlunoComponent,
    AlunoItemComponent,
    AlunoListComponent,
    NewAlunoComponent,
    ProfessorComponent,
    ProfessorItemComponent,
    ProfessorListComponent,
    NewProfessorComponent,
    CursoComponent,
    CursoItemComponent,
    CursoListComponent,
    NewCursoComponent,
    AulaComponent,
    AulaItemComponent,
    AulaListComponent,
    NewAulaComponent,

    HeaderComponent,
    SearchBarComponent,
    NavigatorComponent,
    DeleteButtonComponent
  ],
  imports: [
    BrowserModule,
    HttpModule,
    FormsModule, ReactiveFormsModule,
    RouterModule.forRoot(ROUTES)
  ],
  providers: [
    AuthService,
AlunoService,
ProfessorService,
CursoService,
AulaService,

  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
