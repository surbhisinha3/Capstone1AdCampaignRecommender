FROM python:3.9-slim

WORKDIR /app/

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY app.py /app/
COPY models/model_gender.pkl /app/models/model_gender.pkl
COPY models/model_age_group.pkl /app/models/model_age_group.pkl
COPY models/age_group_test_df.pkl /app/models/age_group_test_df.pkl
COPY models/gender_test_df.pkl /app/models/gender_test_df.pkl
COPY templates/index.html /app/templates/index.html

ENTRYPOINT ["python"]

CMD ["app.py"]

EXPOSE 5001