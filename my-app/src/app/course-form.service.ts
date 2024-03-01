import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { IcourseFormInterface } from './icourse-form.interface';
import { Observable } from 'rxjs';
import { ActivatedRoute } from '@angular/router';

@Injectable({
  providedIn: 'root',
})
export class CourseFormService {
  private serviceBaseUrl = '';
  // id: number = +this.route.snapshot.params['id'];
  constructor(private http: HttpClient, private route: ActivatedRoute) {}
  createCourse(studentData: IcourseFormInterface): Observable<any> {
    console.log('Student Data', studentData);
    return this.http.post<IcourseFormInterface[]>(
      `${this.serviceBaseUrl}/api/students/`,
      {
        course: studentData.course,
        fullname: studentData.fullname,
        email: studentData.email,
        phone: studentData.phone,
      }
    );
  }
}
