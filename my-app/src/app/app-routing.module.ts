import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { CourseListingComponent } from './course-listing/course-listing.component';
import { CourseDetailsComponent } from './course-details/course-details.component';
import { SubscriptionFormComponent } from './subscription-form/subscription-form.component';
import { ContactFormComponent } from './contact-form/contact-form.component';
import { RaptorCourseListComponent } from './raptor-course-list/raptor-course-list.component';


const routes: Routes = [
  { path: 'courses/:id', component: CourseDetailsComponent },
  { path: 'contact-us', component: ContactFormComponent },
  { path: 'courses', component: RaptorCourseListComponent },
  { path: '', component: HomeComponent },  
  // { path: 'course-list', component: CourseListingComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
