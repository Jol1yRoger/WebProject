import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CourseListComponent } from './course-list/course-list.component';
import { CourseDetailComponent } from './course-detail/course-detail.component';

import { CategoryListComponent } from './category-list/category-list.component';
import { LoginComponent } from './login/login.component';

const routes: Routes = [
  { path: '', component: CategoryListComponent },
  { path: 'categories', component: CategoryListComponent },
  { path: 'login', component: LoginComponent },
  { path: 'courses', component: CourseListComponent },
  { path: 'courses/:id', component: CourseDetailComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
